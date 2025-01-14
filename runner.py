from enum import Enum, auto
from glotter import main as glotter_main


class ProjectType(Enum):
    Baklava = auto()
    BinarySearch = auto()
    BubbleSort = auto()
    ConvexHull = auto()
    EvenOdd = auto()
    Factorial = auto()
    Fibonacci = auto()
    FileIO = auto()
    FizzBuzz = auto()
    HelloWorld = auto()
    InsertionSort = auto()
    JobSequencing = auto()
    LCS = auto()
    MergeSort = auto()
    MST = auto()
    Prime = auto()
    QuickSort = auto()
    Quine = auto()
    ROT13 = auto()
    ReverseString = auto()
    RomanNumeral = auto()
    SelectionSort = auto()

    @property
    def key(self):
        return self.name.lower()


def main():
    glotter_main()
#add function
if __name__ == '__main__':
    main()
