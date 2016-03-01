#LAB5#

##CMake:##

###exercise 1:###
    sean@sean-VirtualBox:~/git_repo$ cmake CMakeLists.txt
    
    -- The CXX compiler identification is GNU 4.8.4
    
    -- Check for working CXX compiler: /usr/bin/c++
    
    -- Check for working CXX compiler: /usr/bin/c++ -- works
    
    -- Detecting CXX compiler ABI info
    
    -- Detecting CXX compiler ABI info - done
    
    -- Detecting CXX compile features
    
    -- Detecting CXX compile features - done
    
    -- Configuring done
    
    -- Generating done
    
    -- Build files have been written to: /home/sean/git_repo

###exercise 2:###
  
    sean@sean-VirtualBox:~/git_repo/lab5/ex2_real$ cmake CMakeLists.txt
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/sean/git_repo/lab5/ex2_real
    
    sean@sean-VirtualBox:~/git_repo/lab5/ex2_real$ make
    [ 50%] Built target MathFunctions
    [100%] Built target Tutorial

      
  
###exercise 3:###
  
      sean@sean-VirtualBox:~/git_repo/lab5/ex3$ cmake CMakeLists.txt 
    -- The C compiler identification is GNU 4.8.4
    -- The CXX compiler identification is GNU 4.8.4
    -- Check for working C compiler: /usr/bin/cc
    -- Check for working C compiler: /usr/bin/cc -- works
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Check for working CXX compiler: /usr/bin/c++
    -- Check for working CXX compiler: /usr/bin/c++ -- works
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/sean/git_repo/lab5/ex3
    
        sean@sean-VirtualBox:~/git_repo/lab5/ex3$ make
    Scanning dependencies of target MathFunctions
    [ 50%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
    Linking CXX static library libMathFunctions.a
    [ 50%] Built target MathFunctions
    Scanning dependencies of target Tutorial
    [100%] Building CXX object CMakeFiles/Tutorial.dir/Tutorial.cxx.o
    Linking CXX executable Tutorial
    [100%] Built target Tutorial
    
    sean@sean-VirtualBox:~/git_repo/lab5/ex3$ ctest
    Test project /home/sean/git_repo/lab5/ex3
        Start 1: TutorialRuns
    1/5 Test #1: TutorialRuns .....................   Passed    0.02 sec
        Start 2: TutorialComp25
    2/5 Test #2: TutorialComp25 ...................   Passed    0.02 sec
        Start 3: TutorialNegative
    3/5 Test #3: TutorialNegative .................   Passed    0.02 sec
        Start 4: TutorialSmall
    4/5 Test #4: TutorialSmall ....................   Passed    0.03 sec
        Start 5: TutorialUsage
    5/5 Test #5: TutorialUsage ....................   Passed    0.02 sec
    
    100% tests passed, 0 tests failed out of 5
    
    Total Test time (real) =   0.14 sec


###exercise 4:###

    sean@sean-VirtualBox:~/git_repo/lab5/ex4$ cmake ./
    -- Looking for log
    -- Looking for log - not found
    -- Looking for exp
    -- Looking for exp - not found
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/sean/git_repo/lab5/ex4
    
    sean@sean-VirtualBox:~/git_repo/lab5/ex4$ make
    Scanning dependencies of target MathFunctions
    [ 50%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
    Linking CXX static library libMathFunctions.a
    [ 50%] Built target MathFunctions
    Scanning dependencies of target Tutorial
    [100%] Building CXX object CMakeFiles/Tutorial.dir/Tutorial.cxx.o
    Linking CXX executable Tutorial
    [100%] Built target Tutorial

###exercise 5:###
    
    sean@sean-VirtualBox:~/git_repo/lab5/ex5$ cmake ./
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/sean/git_repo/lab5/ex5

    sean@sean-VirtualBox:~/git_repo/lab5/ex5$ make
    Scanning dependencies of target MathFunctions
    [ 33%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
    Linking CXX static library libMathFunctions.a
    [ 33%] Built target MathFunctions
    Scanning dependencies of target Tutorial
    [ 66%] Building CXX object CMakeFiles/Tutorial.dir/Tutorial.cxx.o
    Linking CXX executable Tutorial
    [ 66%] Built target Tutorial
    Scanning dependencies of target MakeTable
    [100%] Building CXX object MathFunctions/CMakeFiles/MakeTable.dir/MakeTable.cxx.o
    Linking CXX executable MakeTable
    [100%] Built target MakeTable
    
    

  
  
