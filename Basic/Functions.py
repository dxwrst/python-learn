def main():
    default_function()
    function_with_nested()
    function_with_req_param("String")
    function_with_def_param()
    function_with_def_param("def param")
    function_with_def_req_param("req","def")
    function_with_def_req_param("req")
    function_with_named_params(string="a")
    function_with_pos_name_params("pos0","pos1",1,1.5,string="named")

def default_function():
    print("Hello")

def function_with_nested():
    print("Hello from main func body")
    def nested_function():
#        function_with_nested()
        print("Hello fom nested func")
    nested_function()

def function_with_req_param(string):
    print(string)

def function_with_def_param(string = "default"):
    print(string)

def function_with_def_req_param(str,string = "default"):
    print(str, string)

def function_with_named_params(*, string):
    print(string)

def function_with_pos_name_params(*args,string):
    r = ""
    sep = ", "
    for p in args:
        r += str(p)+sep
    r+= string
    print(r)



main()