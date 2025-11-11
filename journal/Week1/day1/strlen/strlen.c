#include <stdio.h>

//function to do the math behind the scenes

int get_strlen(char* word){
    int length = 0;

    // iterate over each and check if its \n
    while (word[length] != '\n'){
        length += 1;

    }
    // if its \n it replaces the \n with \0 it returns
    
    word[length] = '\0';
    return length;
    

}
        
int main(void){
    char sentence[5000];
    printf("enter a string: up to 5000 Characters ");
    fgets(sentence,sizeof(sentence), stdin);
    int num_length = get_strlen(sentence);
    printf("%d",num_length);
    return 0;
    
}


