# class Dogs:
#     paws_number = 4
#     eyes_number = 2
#     nous_number = 1
#     hear_number = 2
#     def show_info(self):
#         print('Количество лап', self.paws_number)
#         print('Количество глаз',self.eyes_number)
#         print('Количество носов',self.nous_number)
#         print('Количество ушей',self.hear_number)
#
#     def get_data(self):
#         a = {
#             'paws_number': self.paws_number,
#             'eyes_number': self.eyes_number,
#             'nous_number': self.nous_number,
#             'hear_number': self.hear_number,
#         }
#
# rex = Dogs() # rex- объект класса Dogs
# print(rex.get_data())
#

#
# class Cats:
#     def __init__(self, name, age, gender):
#         self.paws_number = 4
#         self.eyes_number = 2
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def get_data(self):
#         a = {
#             'paws_number': self.paws_number,
#             'eyes_number': self.eyes_number,
#             'age': self.age,
#             'name': self.name,
#             'gender': self.gender
#         }
#         return a
#
# cotofey = Cats('cotofey', 6, 'men')
# marusya = Cats('marusya', 4, 'woman')
#
# print(cotofey.get_data())
# print(marusya.get_data())

#
class Books:
    def __init__(self,title, author, genre, quantity_of_pages, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity_of_pages = quantity_of_pages
        self.availability = availability

    def get_data(self):
        a = {
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'quantity_of_pages': self.quantity_of_pages,
            'availability': self.availability
        }
        return a

War_and_world = Books('War and world',"Lev Tolstoy", 'roman-ipopea', 1362,  "yes")
Master_and_Margarita = Books('Master and Margarita', "Mikhail Bulgakov", 'roman', 762, "no")

print(War_and_world.get_data())
print(Master_and_Margarita.get_data())


class Books:
    class Tolstoy:

        title = 'Война и мир'
        author = 'Лев Толстой'
        genre = 'роман-ипопея'
        quantity_of_pages = 1362
        availability = 'имеется'

        def show_info(self):
                print('Название:', self.title)
                print('Автор:', self.author)
                print('Жанр:', self.genre)
                print('Количество страниц:', self.quantity_of_pages,'стр.')
                print('Наличие:', self.availability)

    book = Tolstoy()
    print(book.show_info())
    class Bulgakov:
        title = 'Мастер и Маргарита'
        author = 'Михаил Булгаков'
        genre = 'роман'
        quantity_of_pages = 1362
        availability = 'не имеется'

        def show_info(self):
            print('Название:', self.title)
            print('Автор:', self.author)
            print('Жанр:', self.genre)
            print('Количество страниц:', self.quantity_of_pages, 'стр.')
            print('Наличие:', self.availability)


    book = Bulgakov()

    print(book.show_info())


