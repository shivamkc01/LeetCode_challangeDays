class Solution:
    def interpret(self, command: str) -> str:
        """Method : 1"""
#         d = {"(al)":"al", "()":"o","G":"G"}
#         temp = ""
#         res = ""
#         for i in range(len(command)):
#             temp += command[i]
#             if (temp in d):
#                 res += d[temp]
#                 temp = ""
#         return res

        """Cool Method: 2"""
        return command.replace("()", "o").replace("(al)", "al")
        