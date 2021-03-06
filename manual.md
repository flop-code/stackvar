# Stackvar Manual
In this manual you can learn how to use the stackvar programming language.

## First step
To understand how does it work, you need to know about stack data-structure.

How does it work, how to use it, and why do we need it?
If you can give an answer to these questions, then you can go to the next step.

## Idea
Idea of language, that you can use stack, to operate with data.
Of course, you also have variables, and you **should** use them to store permanent data,
but if you need to operate with it, you need to use stack.

Each function have access to stack. It can take data, delete it, and add new data.

So, functions take no arguments, and don't return anything, they take data from stack (as arguments) and push return data to stack (as return value).


## Hello world program
    
First, you need to push a string with "Hello world" to stack.

To do this, just write it.
```
"Hello world!\n"
```

Use "\n" to make a new line.

That's all. Now you have a string in stack.

Next task is to print it.

To do this, you need to call "puts" function.

And all, that you need to do, just write it!
```
puts
```

And now, save it to file, with extension ".stv".

For example as "hello.stv".

So I have this:
```
"Hello world!\n"
puts
```

Now, start it (Use command from [readme.md](README.md))

If you do this right, you should see "Hello world!" in console.

Congratulations! You just wrote your first program in Stackvar!

Tip:

You should separate commands with spaces, except of writing them on new lines.

So, you can write this:
```
"Hello world!\n" puts
```

It will be nicer, if you will use it.

## Math calculations
You can use Stackvar to make math calculations.

Let's write a program, that will calculate a sum of two numbers.

First, you need to push two numbers to stack.

```
4 5
```

Then, you need to call "+" function.

```
+
```

The result will appear in stack.
To print it, use "puts" function.

So, if you will write like this:
```
4 5 + puts
```

And start it, you will see "9" in console.

You can also add a new line.

```
4 5 + puts
"\n" puts
```

Also, remember, that "puts" function takes one element from stack, prints, and **delete** it.

Let me explain how does add function work:
1. It takes first element from stack.
2. It takes second element from stack.
3. It adds them.
4. It pushes result to stack.

It's easy, but remember, that you store elements in stack order.
So first element, that + takes is 4, and second element is 5 (in our case).

It doesn't matter for adding or multiplying, but it does for subtracting or dividing.

So, as I already said, you can also subtract values, multiply them, and divide them.

Operators in Stackvar:
* _+_
* _-_
* _*_
* _/_
* _%_ - division remainder
* _**_ - power


But remember the right order of elements!

If you need to subtract 5 from 4, you need to write this:
```
4 5 -
```

Because - takes 5 (as the last element of stack) and subtract it with 4.

5 - 4 = 1, so it will be pushed to stack.

(You can print it using "puts" function)

Also, in Stackvar, you have "%" function, that will a return remainder of division.

## Stack operations

To operate with stack, you have 7 functions.
* clear - clear the stack.
* isempty - push true to stack, if stack is empty, or push false to stack, if stack is not empty.
* rem - remove last element from stack.
* dup - duplicate last element on stack.
* swap - swap last two elements on stack.
* reverse - reverse stack.
* putsall - print all elements of stack separated by space.

So, for example, if you want to print element, but don't want to delete it, you can use "dup" function.

It will duplicate last element on stack, so puts takes a duplicate of value, and the other one will remain.

To print first element of stack, you can reverse the stack, using following function, and call "dup", and "puts".

And then reverse the stack back.


## Variables
To define a variable in Stackvar, you also need to use stack and push some data to it.

You need to push type of variable first, and name of variable as a string then.

Stackvar Types:
* _INT - integer
* _BOOL - boolean - TRUE of FALSE
* _STRING - string

So, let's define your first Stackvar variable:
```
_INT "my_variable" var
```

As you can see, to define a variable, you need to use a function called "var".

Now, let's push some value into it.
```
5 &my_variable push
```

So, we push a "pointer" to variable first, then the value.

Do not push values, that are different from variable type.

Do not push strings into integer variable, and so on.

If you do this, you will see "WrongTypeError".

To get values from variables, use $[variable]

Example: printing value of variable
```
$my_variable puts
```

## Working with stdin (input data)

To get data from stdin, we can use "read" function.

Data, that you will get from stdin, will be pushed to stack in string type.

Let's write a program, that will calculate sum of two numbers.

First, read the numbers:
```
read read
```

Then call "add" function.
```
+
```

And print the result.
```
puts "\n" puts
```

If we input 5 and 6, we will see 65 in console.

Why? Just because + function can also concatenate strings together.

So how to make integers from strings?

You need to use "cast" function.

First, push the element, that you want to cast to other type, and then push the type.

We are already input data, so we need just to cast it.

Let's cast first string into integer:
```
_INT cast
```

Now, with input 5 and 6, you have stack like this: {"5", 6}

How to cast second string into integer?

Let's swap the elements, and do the same with cast.
```
swap _INT cast swap
```

Now you have stack like this: {5, 6}

And now, you can add them, and print the result.

Let's write a full program:
```
# Reading two numbers
read read

# Cast them to integers
_INT cast
swap
_INT cast
swap

# Adding them together
+

# Add a new line for printing
"\n" swap

# Print them
2 putsm
```

As you can see, wee can use "#" sign, to leave comments in your code, and it will be ignored while execution.

## If-statements
Words, that you write are called "elements".

Each element is standalone.

While compiler translates your code into SVIL, it replace new lines with spaces.

In Stackvar you can store a whole block of code in stack using "Code" type.

To write this standalone block of code
(that of course can operate with stack and variables from main program),
you should use "BEG" and "END" statements.

They mean "Begin" and "End".

Just like "{ }" brackets in other languages.

"if" is just a function that takes boolean value and block of code out from stack,
and executes code, if it sees TRUE, or don't do anything, if it sees FALSE.

For example, let's write a program, that will check, can you drink bear, or not.

Let's imagine, that you can drink beer only after 21.

So, you need to get the age of user, and check if it is greater than 21.

To do this, you should use operators.
You have "=", "!=", ">", "<", ">=", "<=" and so on.

```
read _INT cast  # Read data, and cast it to a number.

BEG
    "Congratulations! You can drink beer!!!" puts
END
21 <= if
```

So what's going on, when we write "21 <= if"?

We already have age on the stack, so we push 21, and check
if 21 is less (or equals) than age.

It is the same with "is age greater (or equals) than 21".

## If-else-statements
You can also write "else" blocks of code, to use them when condition is false.

Let's use the previous program, but print, that user can not drink beer, if age is less than 21.

```
read _INT cast  # Read data, and cast it to a number.

BEG
    "You can not drink beer :(" puts
END
BEG
    "Congratulations! You can drink beer!!!" puts
END
21 <= ifelse
```

As you can see, I used "ifelse" function to do this.

"ifelse" takes boolean value, code to execute if condition is TRUE, and also code, to execute, if condition is FALSE.

You can also write if and if-else statements inside another if/if-else statements.

## While loops

How do you repeat same action multiple times?

Of course, you can copy-paste many lines of code, but you don't need to do this.

Just use while loops!

"while" is a function, that takes not-calculated condition and block of code as a loop body.

"not-calculated condition" is another type in Stackvar.

It stores condition code, so functions can calculate it multiple times.

They have access to variables and other functions.

To write not-calculated condition, write a simple condition, but inside brackets.

Let's print out numbers from 1 to 100 using while loop.

```
_INT "c" var        # Initialize variable c.
1 &c push           # Pushing 1 to c

BEG                 # Loop body:
    $c puts         # Print out c.
    $c 1 + &c push  # Increasing c by 1.
    "\n" puts       # Go to new line.
END                 # End of loop.

(100 $c <=) while   # Pushing not-calculated condition and calling while.

```

## Bitwise operations
Stackvar has all popular operators included bitwise.

* & and
* | or
* ^ xor
* ~ flip bits
* _>>_ right bit shift
* _<<_ left bit shift

## Ending
That's all. You learned a Stackvar language.

To understand it better, try to code in it.

Thanks for reading :)

Bye.