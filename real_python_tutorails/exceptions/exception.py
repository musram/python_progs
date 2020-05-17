
import sys



def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')   
    







if __name__ == "__main__":

    #raise an exception
    #x = 10
    #if x > 5:
    #    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

    #assertion error exception

   
    assert('linux' in sys.platform), "This code runs on Linux only."

    #try-exception block

    try:
        linux_interaction()
        with open('file.log') as file:
             read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except AssertionError as error:
        print(error)
        print('Linux linux_interaction() function was not executed')

    #try-exception-else block   run else if no exceptions 

    try:
        linux_interaction()
    except AssertionError as error:
        print(error)
    else:
       print('Executing the else clause.')


    try:
       linux_interaction()
    except AssertionError as error:
       print(error)
    else:
        try:
            with open('file.log') as file:
              read_data = file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)



    #try-exception-else-finaly block   run finally always

    try:
       linux_interaction()
    except AssertionError as error:
       print(error)
    else:
        try:
            with open('file.log') as file:
              read_data = file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
    finally:
        print('Cleaning up, irrespective of any exceptions.')
