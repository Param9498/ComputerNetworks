#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<math.h>
#include<netinet/in.h>

int main()
{
	int sockfd, serverLength, connfd;

	sockfd=socket(AF_INET, SOCK_STREAM,0);

	if(sockfd>0)
		printf("\nSocket created successfully");

	struct sockaddr_in servaddr;

	servaddr.sin_family=AF_INET;
	servaddr.sin_addr.s_addr=inet_addr("127.0.0.1");
	servaddr.sin_port=6006;

	serverLength=sizeof(struct sockaddr_in);
	connfd=connect(sockfd,(struct sockaddr *)&servaddr, serverLength);
	if(connfd==0)
		printf("\nConnection established successfully..");

	//send message to server
	write(sockfd,"HELLO FROM CLIENT", sizeof("HELLO FROM CLIENT"));

	//recieve a file
	FILE *fp;
	char tempChar;
	fp=fopen("b.txt","w");
	read(sockfd,&tempChar,sizeof(tempChar));
	while(tempChar!=EOF){
		fputc(tempChar,fp);
		read(sockfd,&tempChar,sizeof(tempChar));
	}
	printf("\nFILE RECIEVED");
	fclose(fp);

	//Maths operations
	char operator;
	int operand1,operand2,result;
	printf("\n+ : Addition \n - : Subtraction \n * : Multiplication \n / : Division \n Enter the operator :");
	scanf("%c",&operator);
	printf("\nEnter operands : ");
	scanf("%d %d",&operand1,&operand2);

	write(sockfd,&operator,sizeof(operator));
	write(sockfd,&operand1,sizeof(operand1));
	write(sockfd,&operand2,sizeof(operand2));
	printf("\nWaiting for result..");
	read(sockfd,&result,sizeof(result));
	printf("\nResult : %d %c %d = %d ", operand1,operator,operand2,result);


	//Trigonometry
	int option;
	double angle, trigResult;
	printf("\n 1 : sin \n 2 : cos \n 3 : tan \n");
	scanf("%d",&option);
	printf("\nEnter angle in degrees : ");
	scanf("%lf",&angle);

	write(sockfd,&option,sizeof(option));
	write(sockfd,&angle,sizeof(angle));

	read(sockfd,&trigResult,sizeof(trigResult));
	printf("\nAnswer = %lf", trigResult);

	printf("\nClosing connection...\n");
	close(sockfd);
}



