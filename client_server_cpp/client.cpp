#include <iostream>
#include <netdb.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <sys/socket.h>
#include <fstream>

using namespace std;
int main () {
	struct sockaddr_in client;
	fstream myFile;
	char buffer [1025];
	myFile.open ("Replica.txt", ios::out | ios::binary);

	int sock = socket (AF_INET, SOCK_STREAM, 0);
	client.sin_family = AF_INET;
	client.sin_port = htons (50007);
	inet_pton (AF_INET, "127.0.0.1", &(client.sin_addr));

	connect (sock, (struct sockaddr *) &client, sizeof (client));
	recv (sock, buffer, 1024, 0);

	string file_str = buffer;
	cout << file_str << endl;
	myFile << file_str;
	myFile.close ();

	close (sock);
	return (0);
}
