/*
Encrypter and Decrypter
- Given an image (converted to string) and a key
- Controller will call this to encrypt an image
- Returns an encrypted image as a string
don't even bother trying to compile this
*/

#include <stdio.h>
// imports aes implementation https://github.com/kokke/tiny-AES-C
#include "tiny-AES-C/aes.h"

/* ******************************************************************************************************************************
	Global friends
*/ ******************************************************************************************************************************
#define BSIZE 128	// the image will be divided into blocks of 128 bits
struct htreeArgs {
	int threadID;
	int totalThreads;
	int totalHeight;
	const uint8_t* blockAddr;
};

 // the image will have been converted to a string
 // the code tells whether we need to encrypt or decrypt
 // this code is supposed to get passed to the worker threads but i havent done that here yet
char* main(unsigned char *img, int code) {
	uint32_t numBlocks;		// the number of blocks we will have

	// reads the image and breaks it up into blocks
	char buf[BSIZE];
	int fstatRes = fstat(img, &buf);
	numBlocks = buf.size() / BSIZE;
	if (buf.size() % BSIZE > 0) {
		numBlocks++;
	}
	// reserves memory for the image
	// given write permissions
	// all threads will work on the image
	char *fileAddr = mmap(NULL, buff.size(), PROT_WRITE, MAP_SHARED, img, numBlocks);
	
	// creates a complete binary tree of threads that will each encrypt their given block
	// given n nodes, the height = floor(log_2_n)
	// this will be called htree and each node will be given a structure of arguments (htreeArg)
	// i just like the letter 'h' hehe
	
	pthread_t p1;
	char ret[BSIZE];	// return value. a scrambled block of text will be the same size as before
	// arguments for the first thread
	struct htreeArgs harg = {
		0,
		numThreads,
		treeHeight,
		(const uint8_t*) fileAddr
	};
	
	pthread_create(&p1, NULL, *htree, &harg);
	
	pthread_join(p1, (void **) &ret);
	return 0;
}

// the encryption key will be (size, num rounds):
//		128 bit, 10 rounds; 192 bits, 12 rounds; 256 bits, 14 rounds
*char encrypt(int key, uint64_t length) {
	// import the algorithm. that was like 2000 lines of code man
	// respect to cryptographers for coming up with this 
}

*char decrypt(int key, uint64_t length) {
	// import this 
}

// creating the tree
// takes the struct of its arguments
void* htree(void * arg) {
	struct htreeArgs *hargs = (struct htreeArgs*) arg;
	// will create children as needed
	int lchildExists = 0;
	int rchildExists = 0;
	int lchildPos = (hargs->threadID) * 2 + 1;
	int rchildPos = (hargs->threadID) * 2 + 2;
	// calculates which childre will be made based on position
	// makes children and gives them the encrypt
}