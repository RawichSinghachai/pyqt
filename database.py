from PyQt6.QtSql import QSqlDatabase, QSqlQuery

import uuid

class Database:
    def __init__(self):
        # Ensure we use a unique connection name, e.g., "mainConnection"
        if QSqlDatabase.contains("mainConnection"):
            self.db = QSqlDatabase.database("mainConnection")
        else:
            self.db = QSqlDatabase.addDatabase('QSQLITE', "mainConnection")
            self.db.setDatabaseName('db.sqlite')
            if not self.db.open():
                raise Exception("Failed to open the database")

    def getAdmin(self):
        sql = 'SELECT * FROM Admin;'
        query = QSqlQuery(self.db)
        query.prepare(sql)
        if not query.exec():
            print("Failed to execute query:", query.lastError().text())
            return []

        admins = []
        while query.next():
            admin = {
                'id': query.value(0),           # Assuming the first column is 'id'
                'username': query.value(1),     # Assuming the second column is 'username'
                'email': query.value(2),        # Assuming the third column is 'email'
                'password': query.value(3)      # Assuming the fourth column is 'password'
            }
            admins.append(admin)
        
        self.result = admins
        return admins

    def register(self, username, email, password):
        sql = 'INSERT INTO Admin (Username, Email, Password) VALUES (?, ?, ?);'
        query = QSqlQuery(self.db)
        query.prepare(sql)
        query.addBindValue(username)
        query.addBindValue(email)
        query.addBindValue(password)
        result = query.exec()

        if not result:
            print("Failed to execute query:", query.lastError().text())
        return result

    def checkLogin(self, login, password):
        sql = '''
            SELECT COUNT(*)
            FROM Admin
            WHERE (Username = ? OR Email = ?) AND Password = ?;
        '''
        query = QSqlQuery(self.db)
        query.prepare(sql)
        query.addBindValue(login)  # This will be used for both username and email
        query.addBindValue(login)  # This will be used for both username and email
        query.addBindValue(password)
        
        if not query.exec():
            print("Failed to execute query:", query.lastError().text())
            return False
        
        if query.next():
            count = query.value(0)
            if count > 0:
                print("Login successful")
                return True
            else:
                print("Login failed: Incorrect username/email or password")
                return False
        else:
            print("Query did not return any results")
            return False
    
    def getAllUser(self):
        sql = 'SELECT UserId, FirstName, LastName, Department, Gender, Email, BirthDate FROM User'
        query = QSqlQuery(self.db)
        query.prepare(sql)

        users = []

        if query.exec():
            # Iterate through the query results
            while query.next():
                # Build a dictionary for each row
                user = {
                    'UserId': query.value(0),
                    'FirstName': query.value(1),
                    'LastName': query.value(2),
                    'Department': query.value(3),
                    'Gender': query.value(4),
                    'Email': query.value(5),
                    'BirthDate': query.value(6)  # Convert QDate to string
                }
                users.append(user)
        else:
            print(f"Error executing query: {query.lastError().text()}")

        return users

    
    def createUserDetail(self, userDetail):

        uuid4 = uuid.uuid4()
        
        sql = '''INSERT INTO User (UserId, FirstName, LastName, Department, Gender, Email, BirthDate)
                VALUES (?, ?, ?, ?, ?, ?, ?);'''
        query = QSqlQuery(self.db)
        query.prepare(sql)
        # add uuid
        query.addBindValue(str(uuid4))
        query.addBindValue(userDetail['firstName'])
        query.addBindValue(userDetail['lastName'])
        query.addBindValue(userDetail['department'])
        query.addBindValue(userDetail['gender'])
        query.addBindValue(userDetail['email'])
        query.addBindValue(userDetail['birthDate'])

        if not query.exec():
            print("Failed to execute query:", query.lastError().text())
            return False
        else:
            return True

    def editUserDetail(self,userDetail):
        sql = '''UPDATE User SET FirstName = ? ,LastName = ?, Department = ?,
                Gender = ?, Email = ?, BirthDate = ?
                WHERE UserId = ? ;'''
        
        query = QSqlQuery(self.db)
        query.prepare(sql)

        query.addBindValue(userDetail['firstName'])
        query.addBindValue(userDetail['lastName'])
        query.addBindValue(userDetail['department'])
        query.addBindValue(userDetail['gender'])
        query.addBindValue(userDetail['email'])
        query.addBindValue(userDetail['birthDate'])
        query.addBindValue(userDetail['UserId'])

        if not query.exec():
            print("Failed to execute query:", query.lastError().text())
            return False
        else:
            return True
        
    def deleteUser(self,UserId):
        sql = 'DELETE FROM User WHERE UserID = ?;'
        
        query = QSqlQuery(self.db)
        query.prepare(sql)
        query.addBindValue(UserId)
        if not query.exec():
            print("Failed to execute query:", query.lastError().text())
            return False
        else:
            return True
        

# No self.db.close() calls in individual methods; connection is managed at the class level
