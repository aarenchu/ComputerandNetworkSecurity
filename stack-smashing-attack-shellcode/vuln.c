#include <stdio.h>
#include <string.h>

void func(char *name)
{
    char buf[256];
    printf("%p\n",(void*)&buf); // to get the buffer address
    strcpy(buf, name);
    printf("Hello %s\n", buf);
}

int main(int argc, char *argv[])
{
    func(argv[1]);
    return 0;
}