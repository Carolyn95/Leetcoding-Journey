Data structure: stack, LIFO

Algo: 
```C
OperandType EvaluateExpression(){
    // Calculate the value of an expression (from the gound up)
    // Inplement with two stacks `OPTR`(operator, store value of operators in an expression) `OPND`(operand, store values of operands)
    // OP is the set of all the operators
    InitStack(OPTR); Push(OPTR, '#'); // '#' is the start of an expression
    InitStack(OPDN); cin>>ch;
    while(ch != '#' || GetTop(OPTR) != '#'){
        if (!In(ch, OP)){Push(OPND, ch); cin>>ch;} // func 'In' returns true when ch is an operator
        else
            switch(Precede(GetTop(OPTR), ch)){
                case '<':
                    Push(OPTR, ch); cin>>ch;
                    break;
                case '>':
                    Pop(OPTR, theta);
                    Pop(OPND, b);Pop(OPND, a); // operating order matters
                    Push(OPND, Operate(a, theta, b));
                    break;
                case '=':
                    Pop(OPTR, x); cin>>ch;
                    break;
            }
    }
    return GetTop(OPND);
}
```

Write down each step according to the implementation of above algorithm:

| Steps | OPTR     | OPND  | In character | Operation        |
| -----:|---------:| -----:| ------------:| ----------------:|
|   1    | #       |       |  3\*(7-2)#   | Push(OPND, '3')  |
|   2    | #       |  3    |  \*(7-2)#    | Push(OPTR, '\*') |
|   3    | #\*     |  3    |  (7-2)#      ｜Push(OPTR, '(')  | 
|   4    | #\*(    |  3    |  7-2)#       | Push(OPND, '7')  |
|   5    | #\*(    |  3 7  |  -2)#        | Push(OPTR, '-')  |
|   6    | #\*(-   |  3 7  |  2)#         | Push(OPND, '2')  |
|   7    | #\*(-   |  3 7 2|  )#          | Push(OPND, Operate('7', '-', '2'))|
|   8    | #\*(    |  3 5  |  )#          | Pop(OPTR){deliminate a pair of parathesis}|
|   9    | #\*     |  3 5  |  #           | Push(OPND, Operate('3', '\*', '5'))|
|   10   | #       |  1 5  |  #           | return(GetTop(OPND))|
|        |         |       |              |                  |

