#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char * argv[]) {
	int i; // variable i used as counter
	char *string = 0; // first command line argument will be stored
	char encrypted_string[strlen(string)]; // Computes length of encryption string
	char decrypted_string[strlen(string)]; // Computes length of decryption string
	char *key_ch; // second parameter to the key" "
	char key_int; // key character transformed into an integer

	string = argv[1]; // first command line argument
	key_ch = argv[2]; // second command line argument
	key_int = atoi(key_ch); // transform character into integer

	if (strcmp(argv[3], "encrypt") == 0) { // strcmp = compares strings
		i = 0;
		while (i <= strlen(string) - 1) { // loop to sum string[i] and key_int
			encrypted_string[i] = string[i] + key_int; /* THIS IS THE ENCRYPTION FORMULA */
			i++;
		}
		printf("Encrypted String: \n");
		i = 0;
		while (i <= strlen(string) - 1) {
			printf ("%c", encrypted_string[i]);
			i++;
		}
		printf ("\n");
	}
	if (strcmp(argv[3], "decrypt") == 0) {
		i = 0;
		while (i <= strlen(string) - 1) {
			decrypted_string[i] = string[i] - key_int; /* THIS IS THE DECRYPTION FORMULA */
			i++;
		}
		printf("Decrypted String: ");
		i = 0;
		while (i <= strlen(string) - 1) {
			printf ("%c", decrypted_string[i]);
			i++;
		}
	}
	return EXIT_SUCCESS;
}






