# Static Site Generator in Python

At this point in time I'm about halfway through the creation of the generator.
I've finished making the classes for Text/HTML nodes (plus the leaf / parent nodes
via inheritance) and I'm moving onto the inline elements. We'll need to be able to 
create TextNodes from raw markdown strings. So far, below are some areas I've struggled
with and what I've learned so far.

### Struggles / Steps to solving / Learning:
1. TextType Enums / Class Dunder methods in textnode.py.
Struggle:
I totally forgot how to use enums when I started this section. I've also
never implemented an __eq__ / __repr__ method myself within a class so this was 
fun to play around with and learn for myself. I remembered enums for being useful 
for match / case statements and specifying whether a type is valid or not.

Steps to Solving:
I can create an enum class itself just fine but as a matter of using them, I was for the
most part lost on how they would interact with other sections of my code. I made my own 
little file outside of this project to work out how specifically enums work during interaction / 
match (case) statements. I used cars as an example and did colors as the enum. As for the dunder
methods, I looked up some documentation on how they would work as well as some examples. Within 
each of my classes I created an eq and repr method and printed out some tests to check if they 
worked. Sure enough, they did.

Knowledge gained:
After a bit of playing around, I can say confidently that I'm able to use an enum (especially
within a match case statement.) and can implement my own Dunder methods for classes now!

2. Python's Unittest Library
Struggle:
I've never made my own unittest file outside of just testing a couple different inputs within
the same function on a couple files I've made. 

Steps to solve:
I was introduced to the unittest library from the course I'm learning from (praise Boot.dev)
and they explained some of the basic ways to use it. After checking through the documentation
I can see how its use case is a lot faster / easier than just making your own unittests from scratch.

Knowledge:
I'd say I learned how to really think about edge cases and what kind of things I can do with unit tests.
From bad inputs to really far out there edge cases, (parentnode nesting was pretty weird to me but I'm sure
it's something someone would use) I would say I'm confident in writing my own test cases for code that I've
written now!

3. Recursive call between classes (ParentNode -> LeafNode method call)
Struggle: Recursion between classes that aren't closely "related" via inheritance
I know about recursion and it's cool in some cases. It forces me to think differently
while I'm implementing something. So when the course said I'd be using a recursive method
call within a class I naturally got a little anxious.

Steps to solve:
Within the ParentNode class, the "to html" method was to call leaf node's "to html" method
for each child within the children list. For a second I struggled thinking about how to achieve
this. I started thinking "why can't I just use a for loop and do it within this function?" until
I realized it would be easier to indeed do the recursive call to the child function because each
child of the parent node was just a leaf node. I decided it would be easiest to do each child one
at a time to the function. Part of me thought this wasn't fully recursive because the call could've
had only one child. Then I realized the nesting of parent nodes made this function recursive due to
the nesting.

Knowledge gained:
I'd say a big one was thinking about exactly what objects I was working with at each step within my
functions. The other bit of knowledge would be how to call a different classes method from within 
another class. I did play with classes when I learned OOP but inheritence always seemed odd without
its specific use cases. It was as simple as thinking about what object I was working with, and whether
that object has its own set of functions.

_that's all for now, once I complete another chunk I'll be sure to update readme / push to github!_
