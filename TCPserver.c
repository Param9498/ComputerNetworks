#include<stdio.h>
#include<strings.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<math.h>
#include<netinet/in.h>

void main(int argc, char const *argv[])
{
	int sockfd, clientLength, connfd;

	sockfd=socket(AF_INET, SOCK_STREAM,0);

	if(sockfd>0)
		printf("\nSocket created successfully");

	struct sockaddr_in servaddr;
	struct sockaddr_in clientaddr;

	servaddr.sin_family=AF_INET;
	servadrr.sin_addr.s_addr=INADDR_ANY;
	servaddr.sin_port=6006;

	if(bind(sockfd,(struct socaddr *)&servaddr, sizeof(servaddr))==0)
		printf("\n Bind successfull");

	if(listen(sockfd,5)==0){
		printf("\nSocket listening for connection..");
	}

	clientLength=sizeof(clientaddr);
	connfd=accept(sockfd,(struct socaddr *)&clientaddr,&clientLength);
	if(connfd>0){
		printf("\nConnection accepted successfully");
	}

	//Reading message
	char msg[25];
	read(connfd,&msg,sizeof(msg));
	printf("%s\n",msg);

	//send a file
	FILE *fp;
	char tempChar;
	fp=fopen("a.txt","r");
	tempChar=fgetc(fp);
	while(tempChar!=EOF){
		write(connfd,&tempChar,sizeof(tempChar));
		ch=fgetc(fp);
	}
	write(connfd,&tempChar,sizeof(tempChar));
	printf("\nFILE SENT");
	fclose();

	//Maths operations
	char operator;
	int operand1, operand2, result;
	read(connfd,&operator,sizeof(operator));
	read(connfd,&operand1,sizeof(operand1));
	read(connfd,&operand2,sizeof(operand2));

	switch(operator){
		case '+':result=operand1+operand2;
				break;
		case '-':result=operand1-operand2;
				break;
		case '*':result=operand1*operand2;
				break;
		case '/':result=operand1/operand2;
				break;
		default:
	}
	printf("Result : %d %c %d = %d\n",operand1,operator,operand2,result );

	write(connfd,&result,sizeof(result));

	//trigonometric oprations

	close(sockfd);
}