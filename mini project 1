import pandas as pd
import os
import matplotlib.pyplot as plt

FILE = "movie_booking.csv"

COLUMNS = ["Customer", "Movie", "Tickets", "Price", "Total Amount"]

MOVIES = {
    "Leo": 150,
    "Jailer": 180,
    "GOAT": 200,
    "Coolie": 220,
    "Vidamuyarchi": 170
}

def load_data():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    else:
        return pd.DataFrame(columns=COLUMNS)

def save_data(df):
    df.to_csv(FILE, index=False)

def book_ticket():
    df = load_data()

    name = input("Enter Customer Name: ")

    print("\nAvailable Movies")
    movie_list = list(MOVIES.keys())

    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie} - Rs.{MOVIES[movie]}")

    try:
        choice = int(input("Choose Movie: "))
        movie = movie_list[choice - 1]
    except:
        print("Invalid Choice")
        return

    tickets = int(input("Enter Number of Tickets: "))

    price = MOVIES[movie]
    total = price * tickets

    new_row = pd.DataFrame([[name, movie, tickets, price, total]],
                           columns=COLUMNS)

    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)

    print("\nTicket Booked Successfully!")
    print("Total Amount = Rs.", total)

def view_bookings():
    df = load_data()

    if df.empty:
        print("No Bookings Found")
    else:
        print(df)

def analyze():
    df = load_data()

    if df.empty:
        print("No Data Available")
        return

    print("\nTotal Collection: Rs.", df["Total Amount"].sum())

    print("\nTickets Sold")
    print(df.groupby("Movie")["Tickets"].sum())

def show_graph():
    df = load_data()

    if df.empty:
        print("No Data Available")
        return

    graph = df.groupby("Movie")["Tickets"].sum()

    graph.plot(kind="bar")
    plt.title("Movie Ticket Sales")
    plt.xlabel("Movie")
    plt.ylabel("Tickets Sold")
    plt.show()

def search_booking():
    df = load_data()

    name = input("Enter Customer Name: ")

    result = df[df["Customer"].str.lower() == name.lower()]

    if result.empty:
        print("Booking Not Found")
    else:
        print(result)

def main():
    while True:
        print("\n===== MOVIE TICKET BOOKING SYSTEM =====")
        print("1. Book Ticket")
        print("2. View Bookings")
        print("3. Search Booking")
        print("4. Analyze Collection")
        print("5. Show Graph")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            book_ticket()

        elif choice == "2":
            view_bookings()

        elif choice == "3":
            search_booking()

        elif choice == "4":
            analyze()

        elif choice == "5":
            show_graph()

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

main()
