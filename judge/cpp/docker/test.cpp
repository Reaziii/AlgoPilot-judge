#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
int main(int argc, char* argv[]) {
    std::string __time = argv[1], __memory = argv[2];
    system("rm -rf a.out");
    system("g++ main.cpp -o a.out");
    std::ifstream __inputFile("./a.out");
    if (!__inputFile.is_open())
    {
        printf("3");
        return 0;
    }
    std::string command = "TIME_LIMIT="+__time+"\nMEMORY_LIMIT="+__memory+"\ntimeout \"$TIME_LIMIT\" bash -c \"ulimit -v $MEMORY_LIMIT && ./a.out < input > output\"\necho $? > result";
    int result = system(command.c_str());
    if(result!=0){
        // execution failed
        printf("6");
        return 0;
    }
    std::ifstream inputFile("./result");
    if (!inputFile.is_open())
    {
        printf("6");
        return 0;
    }
    std::string line, ans;
    while (std::getline(inputFile, line))
    {
        break;
    }

    inputFile.close();
    if (line == "124")
    {
        // time limit exceed
        printf("1");
        return 0;
    }
    else if (line == "126")
    {
        // compilation error
        printf("3");
        return 0;
    }
    else if (line == "139")
    {
        // run time error
        printf("2");
        return 0;
    }
    else if (line == "0")
    {
        // exceution successfull
        printf("0\n");
        std::ifstream inputFile("./output");
        if (!inputFile.is_open())
        {
            std::cerr << "6";
            return 1;
        }
        std::string line, ans;
        while (std::getline(inputFile, line))
        {
            std::cout<<line<<std::endl;
        }
        inputFile.close();
    }

    return 0;
}