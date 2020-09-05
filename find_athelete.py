from datetime import datetime
from users import User
from users import Athelete
from users import connect_db

def find():
    session = connect_db()

    find_id = input("Ввведите идентификатор пользователя: ")
    user = session.query(User).filter(User.id == find_id).first()
    
    atheletes = session.query(Athelete).filter(Athelete.birthdate).all()
    atheletes_height = session.query(Athelete).filter(Athelete.height).all()


    session.close()

    if user:
        candidate1 = atheletes[0]
        candidate2 = atheletes[1]

        for athelete in atheletes:
            
            date1 = datetime.strptime(athelete.birthdate, '%Y-%m-%d')
            date2 = datetime.strptime(user.birthdate, '%Y-%m-%d')
            date3 = datetime.strptime(candidate1.birthdate, '%Y-%m-%d')
            diff_athelete = abs(date1-date2).days
            diff_candidate1 = abs(date3-date2).days
            if diff_athelete < diff_candidate1: 
                candidate2 = candidate1
                candidate1 = athelete
                            
        print ("Первый атлет-" + candidate1.name, candidate1.birthdate, "\nВторой атлет-" + candidate2.name, candidate2.birthdate)    

        candidate_height = atheletes_height[0]
        for ath_height in atheletes_height:
            diff_athelete_height = abs(ath_height.height-user.height)
            diff_candidate_height = abs(candidate_height.height-user.height)
            if diff_athelete_height < diff_candidate_height:
                candidate_height = ath_height
        print (candidate_height.name, candidate_height.height)

         
    else:
        print ("Пользователя с таким идентификатором нет")


if __name__ == "__main__":
    find()