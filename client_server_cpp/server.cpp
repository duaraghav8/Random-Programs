#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <fstream>

using namespace std;
void handle_client (void) {
	int sock = socket (AF_INET, SOCK_STREAM, 0);
	struct sockaddr_in server;
	string file_str;
	fstream myFile;

	myFile.open ("myfile.txt", ios::in | ios::binary);
	myFile >> file_str;
	myFile.close ();
	cout << "String to be sent to the client: " << file_str << endl;

	server.sin_family = AF_INET;
	server.sin_port = htons (50007);
	server.sin_addr.s_addr = INADDR_ANY;
//	inet_pton (AF_INET, "172.16.13.187", & (server.sin_addr));

	bind (sock, (struct sockaddr *) &server, sizeof (server));
	listen (sock, 4);

	while (true) {
//		int client = accept (sock, (struct sockaddr *) &client_ad, &client_s );
		int client = accept (sock, NULL, NULL);
//		cout << "Connected to " << inet_ntoa (client_ad.sin_addr) << endl;

		send (client, file_str.c_str (), file_str.length (), 0);

		close (client);
		break;
	}
}

int main () {
	handle_client ();
	return (0);
}
