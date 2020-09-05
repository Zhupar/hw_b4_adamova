import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()


class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'user'

    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.INTEGER, primary_key="True")
    # имя пользователя
    first_name = sa.Column(sa.Text)
    # фамилия пользователя
    last_name = sa.Column(sa.Text)
    # пол пользователя
    gender = sa.Column(sa.Text)
    # адрес электронной почты пользователя
    email = sa.Column(sa.Text)
    # дата рождения пользователя
    birthdate = sa.Column (sa.Text)
    # рост пользователя
    height = sa.Column (sa.REAL)

class Athelete(Base):
    # Название таблицы
    __tablename__ = "athelete"
    # Идентификатор атлета
    id = sa.Column(sa.Integer, primary_key=True)
    # Дата рождения
    birthdate = sa.Column(sa.Text)
    # Рост атлета
    height = sa.Column(sa.REAL)
    # Имя атлета
    name = sa.Column(sa.Text)
 

def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    # выводим приветствие
    print("Привет! Я запишу твои данные!")
    # запрашиваем у пользователя данные
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    
    gender_input = input("Введите свой пол 'Male'(мужской) /'Female'(женский):")
    while (gender_input!='Male') and (gender_input!='Female'):  
        gender_input = input("Введите свой пол 'Male'(мужской) /'Female'(женский):")
    gender = gender_input   

    
    email_input = input("Мне еще понадобится адрес твоей электронной почты: ")
    if email_input.count('@') == 1:
        mail = email_input.split('@')
        domain = mail[1]
        if domain.find('.') ==-1:
            email_input = input("Повтори адрес электронной почты: ")
        else:
            email = email_input
    else:
        email_input = input("Повтори адрес электронной почты: ")


    birthday_input = input("Введи дату рождения YYYY-MM-DD: ")
    birthday_list = birthday_input.split('-')    
    while len(birthday_list) != 3:
        birthday_input = input("Введи дату рождения YYYY-MM-DD: ")
        birthday_list = birthday_input.split('-')
    while int(birthday_list[0]) < 1000 or int(birthday_list[0]) > 2020 or int(birthday_list[1]) < 0 or int(birthday_list[1]) > 13 or int(birthday_list[2]) < 0 or int(birthday_list[2]) > 32:
        birthday_input = input("Введи дату рождения YYYY-MM-DD: ")
        birthday_list = birthday_input.split('-')         
    birthdate = birthday_input

        
    height = input("Какой у тебя рост? ")

    # создаем нового пользователя
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    # возвращаем созданного пользователя
    return user

def connect_db():
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()




def main():
    
    session = connect_db()
    # запрашиваем данные пользоватлея
    user = request_data()
    # добавляем нового пользователя в сессию    
    session.add(user)
    # сохраняем все изменения, накопленные в сессии
    session.commit()
    print("Спасибо, данные сохранены!")
    # поиск ближайшего к пользователю атлета
    

if __name__ == "__main__":
    main()
    
