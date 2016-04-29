#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]) {
    FILE *fp1, *fp2;
    char* key;
    int c;

    key = argv[1];

    if (*key != '\0') {
        fp1 = fopen(argv[2],"rb");
        if (fp1 != NULL) {
            fp2 = fopen(argv[3],"wb");
            if (fp2 != NULL) {
                while (((c=getc(fp1))!=EOF)) {
                    if (!*key)key = argv[1];
                    c ^=*(key++);
                    putc(c, fp2);
                }
            fclose(fp2);
            }
        fclose(fp1);
        }
    }
return 1;
}