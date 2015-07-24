__author__ = 'mark'
str1 = "Geeksdas"
str2 = ":Geeksdas"


class Longest:
    max_value = 0

    def longest_sub_string(self, str1, str2, i, j, temp):
        str1_len = len(str1)
        str2_len = len(str2)
        if i >= str1_len:
            return 0
        if j >= str2_len:
            return 0
        if str1[i] == str2[j]:
            temp += 1
            if self.max_value < temp:
                self.max_value = temp
            self.longest_sub_string(str1, str2, i + 1, j + 1, temp)

        else:
            self.longest_sub_string(str1, str2, i + 1, j, 0)
            self.longest_sub_string(str1, str2, i, j + 1, 0)


test = Longest()
test.longest_sub_string(str1, str2, 0, 0, 0)
print test.max_value
