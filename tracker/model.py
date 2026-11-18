# import tokenize, io
# # for t in tokenize.generate_tokens(io.StringIO("x = 1 + 2\n").readline):
# #     print(t)

# for t in tokenize.generate_tokens(io.StringIO("abc def").readline):
#     print(t)

# print("\n")
# print("\n")

# import ast; 
# print(ast.dump(ast.parse("x = 1 + 2"), indent=2))

# print("\n")
# print("\n")

import dis; 
# dis.dis("x = 7 + 3")

# print("\n")
# print("\n")

# def f(a: int):
#     return a + 1

# print(list(f.__code__.co_code))   # raw bytecode bytes, just numbers

# print("\n")
# print("\n") 

# dis.dis('print(a+b)')                        # the human-readable version

# c = compile("print(a+b+c)", "x", "exec")
# print(list(c.co_code))
# dis.dis(c)


# dis.dis(compile("a + b", "<s>", "single"))   # ends with a print instruction
# dis.dis(compile("a + b", "<s>", "exec"))     # ends with POP_TOP

import ast
print(ast.dump(ast.parse("x = a + b"), indent=2))