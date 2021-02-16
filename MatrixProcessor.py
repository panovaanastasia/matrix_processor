class Matrices:
    def __init__(self):
        self.exit = 0
    def work(self):
        while self.exit != 1:
            print('1. Add matrices')
            print('2. Multiply matrix by a constant')
            print('3. Multiply matrices')
            print('4. Transpose matrix')
            print('5. Calculate a determinant')
            print('6. Inverse matrix')
            print('0. Exit')
            choice = input('Your choice: ')
            if choice == '1':
                self.add()
                print()
            elif choice == '2':
                self.m_constant()
                print()
            elif choice == '3':
                self.m_matrices()
                print()
            elif choice == '4':
                self.transpose()
                print()
            elif choice == '5':
                self.determinant()
                print()
            elif choice == '6':
                self.inverse()
                print()
            elif choice == '0':
                self.exit = 1
    def add(self):
        m1, n1 = input('Enter size of first matrix: ').split()
        first_matrix = []
        second_matrix = []
        print('Enter first matrix:')
        for i in range(int(m1)):
            a = []
            a = input().split()
            first_matrix.append(a)
        m2, n2 = input('Enter size of second matrix: ').split()
        print('Enter second matrix:')
        for i in range(int(m2)):
            a = []
            a = input().split()
            second_matrix.append(a)
        if m1 != m2 or n1 != n2:
            print('The operation cannot be performed.')
        else:
            print('The result is:')
            for i in range(int(m1)):
                for j in range(int(n1)):
                    if first_matrix[i][j].find('.') == -1 and second_matrix[i][j].find('.') == -1:
                        first_matrix[i][j] = str(int(first_matrix[i][j]) + int(second_matrix[i][j]))
                    else:
                        first_matrix[i][j] = str(float(first_matrix[i][j]) + float(second_matrix[i][j]))
                print(" ".join(first_matrix[i]))
    def m_constant(self):
        m1, n1 = input('Enter size of matrix: ').split()
        first_matrix = []
        print('Enter matrix:')
        for i in range(int(m1)):
            a = []
            a = input().split()
            first_matrix.append(a)
        number = input('Enter constant: ')
        if number.find('.') == -1:
            number = int(number)
        else:
            number = float(number)
        print('The result is:')
        for i in range(int(m1)):
            for j in range(int(n1)):
                if first_matrix[i][j].find('.') == -1:
                    first_matrix[i][j] = str(int(first_matrix[i][j]) * number)
                else:
                    first_matrix[i][j] = str(float(first_matrix[i][j]) * number)
            print(" ".join(first_matrix[i]))
    def m_matrices(self):
        m1, n1 = input('Enter size of first matrix: ').split()
        first_matrix = []
        second_matrix = []
        print('Enter first matrix:')
        for i in range(int(m1)):
            a = []
            a = input().split()
            first_matrix.append(a)
        m2, n2 = input('Enter size of second matrix: ').split()
        print('Enter second matrix:')
        for i in range(int(m2)):
            a = []
            a = input().split()
            second_matrix.append(a)
        if n1 != m2:
            print('The operation cannot be performed.')
        else:
            for i in range(int(m1)):
                a = []
                for j in range(int(n2)):
                    s = 0
                    for k in range(int(n1)):
                        if first_matrix[i][k].find('.') == -1 and second_matrix[k][j].find('.') == -1:
                            s += int(first_matrix[i][k]) * int(second_matrix[k][j])
                        else:
                            s += float(first_matrix[i][k]) * float(second_matrix[k][j])
                    a.append(str(s))
                print(" ".join(a))
    def transpose(self):
        print()
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        choice = input('Your choice: ')
        m1, n1 = input('Enter size of matrix: ').split()
        m1 = int(m1)
        n1 = int(n1)
        first_matrix = []
        print('Enter matrix:')
        for i in range(int(m1)):
            a = []
            a = input().split()
            first_matrix.append(a)
        print('The result is:')
        if choice == '1':
            for i in range(n1):
                a = []
                for j in range(m1):
                    a.append(first_matrix[j][i])
                print(" ".join(a))
        elif choice == '2':
            for i in range(n1):
                a = []
                for j in range(m1):
                    a.append(first_matrix[m1 - 1 - j][n1 - 1 - i])
                print(" ".join(a))
        elif choice == '3':
            for i in range(m1):
                a = []
                for j in range(n1):
                    a.append(first_matrix[i][n1 - 1 - j])
                print(" ".join(a))
        elif choice == '4':
            for i in range(m1):
                a = []
                for j in range(n1):
                    a.append(first_matrix[m1 - 1 - i][j])
                print(" ".join(a))
    def determinant(self):
        m1, n1 = input('Enter size of matrix: ').split()
        first_matrix = []
        print('Enter matrix:')
        for i in range(int(m1)):
            a = []
            a = input().split()
            first_matrix.append(a)
        print('The result is:')
        for i in range(int(m1)):
            for j in range(int(n1)):
                if first_matrix[i][j].find('.') == -1:
                    first_matrix[i][j] = int(first_matrix[i][j])
                else:
                    first_matrix[i][j] = float(first_matrix[i][j])
        print(det(first_matrix))
    def inverse(self):
        m1, n1 = input('Enter size of matrix: ').split()
        m1 = int(m1)
        n1 = int(n1)
        first_matrix = []
        print('Enter matrix:')
        for i in range(int(m1)):
            a = []
            a = input().split()
            first_matrix.append(a)
        for i in range(int(m1)):
            for j in range(int(n1)):
                if first_matrix[i][j].find('.') == -1:
                    first_matrix[i][j] = int(first_matrix[i][j])
                else:
                    first_matrix[i][j] = float(first_matrix[i][j])
        if det(first_matrix) == 0:
            print("This matrix doesn't have an inverse.")
        else:
            matrix = []
            for i in range(m1):
                a = []
                for j in range(n1):
                    x = []
                    for k in range(m1):
                        if k != i:
                            x.append(first_matrix[k][:j] + first_matrix[k][j+1:])
                    a.append(pow(-1, i+j) * det(x))
                matrix.append(a)
            for i in range(n1):
                a = []
                for j in range(m1):
                    a.append(str((1/det(first_matrix)) * matrix[j][i]))
                print(" ".join(a))
                
            

def det(a):
    if len(a) == 1:
        return a[0][0]
    if len(a) == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    else:
        s = 0
        for i in range(len(a[0])):
            x = []
            for j in range(1, len(a[0])):
                x.append(a[j][:i] + a[j][i+1:])
            s += pow(-1, i) * det(x) * a[0][i]
        return s

matrix = Matrices()
matrix.work()
