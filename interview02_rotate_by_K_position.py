class problem:
    @classmethod
    def rotatearr(cls,arr,k):
        n = len(arr)-1
        cls.revarr(arr, 0, k-1)
        cls.revarr(arr, k, n)
        cls.revarr(arr,0,n)

    @classmethod
    def revarr(cls,arr,start,end):

        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    @classmethod
    def main(cls):
        arr = [1,2,3,4,5,6,7,8,9]
        cls.rotatearr(arr,3)
        print(arr)


if __name__ == "__main__":
    problem.main()
