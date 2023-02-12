from typing import List

class Aircraft_Seat_Allocation:

    def __init__(self):
        self.seats: List[List[int]] = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.get_seat_aphabet = {
            0: "a",
            1: "b",
            2: "c",
            3: "d",
            4: "e",
            5: "f",
            6: "g",
            7: "h"
        }
        self.get_seat_number = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7
        }

    def allocate_seats(self, number_of_seats: int):
        seats: List[str] = []
        if number_of_seats == 4:
            # print("4")
            seats = self.allocate_four_seat()
        if number_of_seats == 3:
            # print("3")
            seats = self.get_three_seat_allocation()
        if number_of_seats == 2:
            # print("2")
            seats = self.get_two_seat_allocation()
        if number_of_seats == 1:
            # print("1")
            seats = self.get_one_seat_allocation()
        print(number_of_seats,seats)

    def allocate_four_seat(self) -> List[str]:
        allocated_seats: List[str] = self.get_four_seat_allocation()
        if allocated_seats.__len__() != 4:

            first_pair = self.get_two_seat_allocation()
            second_pair = self.get_two_seat_allocation()

            allocated_seats = first_pair + second_pair

            if allocated_seats.__len__() != 4:
                allocated_seats = []
        return allocated_seats

    def get_four_seat_allocation(self) -> List[str]:

        middle_seat: List[int] = [2, 3, 4, 5]
        allocated_seats: List[str] = []
        for row in range(self.seats.__len__()):
            for column in range(self.seats[row].__len__()):
                if column in middle_seat and not self.seats[row][column]:
                    allocated_seats.append(
                        str(row+1)+self.get_seat_aphabet[column])
                    self.seats[row][column] = 1

            if allocated_seats.__len__() == 4:
                break
            else:
                self.reset_allocated_seats(allocated_seats)
                allocated_seats = []
        return allocated_seats

    def get_three_seat_allocation(self) -> List[str]:
        allocated_seats: List[str] = []
        middle_seats: List[int] = [2, 3]

        for row in range(self.seats.__len__()):
            # print(row)
            for column in middle_seats:
                # print("col : ",column)
                if not self.seats[row][column] and not self.seats[row][column+1] and not self.seats[row][column+2]:
                    allocated_seats.append(
                        str(row+1)+self.get_seat_aphabet[column])
                    allocated_seats.append(
                        str(row+1)+self.get_seat_aphabet[column+1])
                    allocated_seats.append(
                        str(row+1)+self.get_seat_aphabet[column+2])
                    self.seats[row][column] = 1
                    self.seats[row][column+1] = 1
                    self.seats[row][column+2] = 1
                    return allocated_seats

        return allocated_seats

    def get_two_seat_allocation(self) -> List[str]:
        allocated_seats: List[str] = []
        corners: List[int] = [0, 6]

        for row in range(self.seats.__len__()):
            # print("row : ", row)
            for column in corners:
                # print(column)
                if not self.seats[row][column] and not self.seats[row][column+1]:
                    allocated_seats.append(
                        str(row+1)+self.get_seat_aphabet[column])
                    allocated_seats.append(
                        str(row+1)+self.get_seat_aphabet[column+1])
                    self.seats[row][column] = 1
                    self.seats[row][column+1] = 1
                    return allocated_seats
        return allocated_seats

    def get_one_seat_allocation(self) -> List[str]:

        allocated_seat: List[str] = []

        for row in range(self.seats.__len__()):
            # print("row: ", row)
            for column in range(self.seats[row].__len__()):
                # print(column)
                if not self.seats[row][column]:
                    allocated_seat.append(
                        str(row+1)+self.get_seat_aphabet[column])
                    self.seats[row][column] = 1
                    return allocated_seat

        return allocated_seat

    def reset_allocated_seats(self, allocated_seats: List[str]):
        for seat in allocated_seats:
            row: int = int(seat[0])
            column: int = self.get_seat_number[seat[1]]
            self.seats[row-1][column] = 0


input: List[int] = [4,3,3,2,2,4,1]
obj: Aircraft_Seat_Allocation = Aircraft_Seat_Allocation()
for i in input:
    obj.allocate_seats(i)
