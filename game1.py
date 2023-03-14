""" Game Walk task 6"""

class Character:
    """ General character class """
    def __init__(self, name, aggresive = False) -> None:
        self.name = name
        self.aggresive = aggresive

class Friend(Character):
    """ Positive character """
    def __init__(self, name) -> None:
        """ Init method """
        super().__init__(name)
        self.talk_text = ""

    def set_talk(self, talk):
        """ Sets talk to particular character """
        self.talk_text = talk

    def talk(self):
        """ Talk with character """
        print(self.talk_text)

class Advisor(Friend):
    """ Student class """
    def __init__(self, name) -> None:
        super().__init__(name)

class Giver(Friend):
    """ Giver class """
    def __init__(self, name, like, talk_success, talk_failure) -> None:
        super().__init__(name)
        self.like = like
        self.item = ""
        self.talk_success = talk_success
        self.talk_failure = talk_failure

    def treat(self, item):
        """ This function returns true if character likes item and false if not """
        if self.like == item:
            return True
        return False

    def set_item(self, item):
        """ This method sets item to character"""
        self.item = item


class Enemy(Character):
    """ Negative character """
    def __init__(self, name, weakness, aggresive):
        """ Init inctance """
        super().__init__(name, aggresive)
        self.weakness = weakness

    def defence(self, item_defence):
        """ Defence aginst character """
        if self.weakness == item_defence:
            return True
        return False

class Shbuy(Enemy):
    """ Bully class """
    def __init__(self, name, weakness):
        super().__init__(name, weakness, True)

class TypicalBoss(Enemy):
    """ Boss class """
    def __init__(self, name, weakness, question, answer, first_stage_success,
                 second_stage_success, second_stage_failure):
        super().__init__(name, weakness, True)
        self.question = question
        self.answer = answer
        self.first_stage_success = first_stage_success
        self.second_stage_success = second_stage_success
        self.second_stage_failure = second_stage_failure

    def answer_question(self, answer):
        """ Returns True if answer is correct and false if not"""
        if self.answer == answer:
            return True
        return False

class Street:
    """ Street class"""
    def __init__(self, name) -> None:
        self.name = name
        self.item = None
        self.linked_rooms = {}
        self.character = None
        self.description = ""

    def link_room(self, street, direction):
        """
        This method links streets to another
        throught dictionary with key - direction and value - street"""
        self.linked_rooms[direction] = street
    def set_character(self, character):
        """ This method sets character for particular street """
        self.character = character
    def get_item(self):
        """ Return item on the street """
        return self.item
    def set_item(self, item):
        """ This method sets character for particular street """
        self.item = item
    def set_description(self, description):
        """ This method sets description """
        self.description = description

    def get_details(self):
        """ This method returns details about street """
        print("")
        print("***************")
        print(f"{self.name}")
        print("--------------------")
        print("")
        # print(self.description)
        for direction, place in self.linked_rooms.items():
            if direction == "вперед":
                print(f"{place.name} попереду")
            else:
                print(f"{place.name} позаду")
        if self.item is not None:
            self.item.describe()
        if self.character is not None:
            print(f"{self.character.name} на вулиці")
    def get_character(self):
        """ This method returns character on specific street """
        return self.character

    def move(self, direction):
        """ Make move to specific direction """
        if direction not in self.linked_rooms:
            return self
        return self.linked_rooms[direction]

class Item:
    """ General Item class"""
    def __init__(self,name) -> None:
        """ Init method """
        self.description = ""
        self.name = name

    def set_description(self, description):
        """ This method sets description to item """
        self.description = description
    def describe(self):
        """ This method describes item"""
        print(f"[{self.get_name()}] - {self.description}")
    def get_name(self):
        """ This method returns name of item """
        return self.name

# srtiyskya street
srtiyskya = Street("вул. Стрийська")
srtiyskya.set_description("Вулиця Стрийська одна з найдовших (близько 7,5 км)")


flower = Item("квіти")
flower.set_description("Дуже рідкісні квіти з найвищих точок Карпат.")

srtiyskya.set_item(flower)

student_Andrew = Advisor("Андрій")
student_Andrew.set_talk("Хей, як справи? До речі, оце улюблені квіти пані Надія")

srtiyskya.set_character(student_Andrew)

franka = Street("вул. І.Франка")

srtiyskya.link_room(franka, "вперед")
franka.link_room(srtiyskya, "назад")


giver = Giver("Пані Надії", "квіти", "Дуже дякую це мої улюблені. Візьми магічне [зілля],\
 воно тобі точно знадобиться.", "Дякую, але мені це не знадобиться")
poution = Item("зілля")
giver.set_item(poution)

franka.set_character(giver)

suit = Item("плащ")
suit.set_description("В ньому дуже легко сховатися в натовпі.")
franka.set_item(suit)


shevchenka = Street("пр.Т.Шевченка")
franka.link_room(shevchenka, "вперед")
shevchenka.link_room(franka, "назад")

bully = Shbuy("Збуй", "плащ")
shevchenka.set_character(bully)


boss = TypicalBoss("Розбійник", "зілля",\
 "Куди тікати в будинок чи на головну площу? (1 - будинок, 2 - головна площа)", "1",\
 "Вам вдалося відбитися, але вам доведеться вибрати щлях для відступу",
 "Вам вдалося пересидіти в будинку і дочeкатися поліції",
 "По дорозі до площі вас перехопили і пограбувати")


krakivska = Street("вул. Краківська")
krakivska.link_room(shevchenka, "назад")
krakivska.set_character(boss)
shevchenka.link_room(krakivska, "вперед")


current_street = srtiyskya

print("*** Гра блукачка по Львову ***")

print(""" Напишіть:

"вперед", щоб перейти на вулицю попереду
"назад", щоб перейти на вулицю позаду
"говорити", щоб поговорити з персонажом на вулиці
"взяти", щоб взяти предмет на вулиці
"подарувати", що подарувати обраний предмет песонажу на вулиці
""")
print("Речі, які є в вашому рюкзаку не будуть\
 показані навмисно, щоб ви їх запам'ятовували, було цікавіше грати")

backpack = []
while True:

    current_street.get_details()
    character = current_street.get_character()
    if character and character.aggresive:
        print(f"!!!!! На вас напав {character.name} !!!!!")
        print("Оберіть предмет, яким ви будете захищатися.")

        defence_item = input("> ")
        if defence_item in backpack and character.defence(defence_item):
            if isinstance(character, TypicalBoss) and character.question:
                print(character.first_stage_success)
                print(character.question)
                way_decision = input("> ")
                if character.answer_question(way_decision):
                    print(character.second_stage_success)
                    print("Вітаємо ви пройшли гру)!!!!!")
                    break
                else:
                    print(character.second_stage_failure)
                    print("Ви програли(")
                    break

            print("У вас вийшло врятуватися!!!")
            current_street.set_character(None)
            backpack.remove(defence_item)
            continue
        elif defence_item not in backpack:
            print(f"""У вас немає такого предмету. На жаль,\
 {character.name} не зрозумів ваших жартів. Ви програли(""")
            break
        else:
            print(f"На жаль, {character.name} не зрозумів ваших жартів. Ви програли(")
            break


    decision = input(">>> ")
    if decision in ("вперед", "назад"):
        current_street = current_street.move(decision)
    elif decision == "говорити":
        character = current_street.get_character()
        if character is not None and isinstance(character, Advisor):
            character.talk()
        else:
            print("Не можна ні з ким поговорити")
    elif decision == "взяти":
        item = current_street.get_item()
        if item is not None:
            print(f"Предмет [{item.name}] доданий в рюкзак")
            backpack.append(item.name)
            current_street.set_item(None)
        else:
            print("Не можна нічого взяти")
    elif decision == "подарувати":
        if character and isinstance(character, Giver):
            print("Введіть назву предмета, який ви хочете подарувати")
            present = input("> ")
            if present in backpack and character.treat(present):
                print(character.talk_success)
                current_street.set_character(None)
                backpack.append(character.item.name)
                backpack.remove(present)
                continue
            elif present not in backpack:
                print("У вас немає такого предмету.")
            else:
                print(f"{character.talk_failure}")
        else:
            print("Не можна нічого подарувати")
