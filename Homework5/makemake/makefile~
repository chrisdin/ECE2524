#Christopher Din
#Homework 5: create a makefile

CC = g++
CFlags = -Wall -g
OBJS = exprtest

#____________all_____________
all: exprtest
#_________exprtest___________
driver.cpp: scanner.hpp driver.hpp
scanner.hpp: parser.tab.hpp
parser.tab.hpp parser.tab.cpp: parser.ypp        
parser.tab.cpp: expression.hpp scanner.hpp driver.hpp
scanner.cpp: scanner.ll
#_________clean______________
clean:
    rm -f *.o *~ core tmp 
    rm -f exprtest
    rm -f location.hh
    rm -f position.hh
    rm -f parser.tab.cpp
    rm -f scanner.cpp
    rm -f stack.hh
  
