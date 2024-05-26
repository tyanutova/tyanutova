from PIL import Image
cards = {
    "Birthday": "birthday_card.jpg",
    "New Year": "new_year_card.jpg",
    "Valentine's Day": "valentines_day_card.jpg"
}
def show_card(holiday):
    if holiday in cards:
        file_name = cards[holiday]
        card = Image.open(file_name)
        card.show()
    else:
        print("Card for this holiday not found.")
holiday = input("For which holiday do you need a card? ")
show_card(holiday)
