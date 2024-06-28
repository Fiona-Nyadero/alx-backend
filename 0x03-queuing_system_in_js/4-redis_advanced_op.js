import redis from 'redis';

const client = redis.createClient();

// Handles connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

function createAndDisplayHash() {
	//Create Hash using hset
	client.hset('HolbertonSchools', 'Portland', '50', redis.print);
	client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
	client.hset('HolbertonSchools', 'New York', '20', redis.print);
	client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
	client.hset('HolbertonSchools', 'Cali', '40', redis.print);
	client.hset('HolbertonSchools', 'Paris', '2', redis.print);

	//Display Hash using hgetall
	client.hgetall('HolbertonSchools', (err, reply) => {
		if (err) {
			console.error('Error retrieving hash:', err);
		} else {
			console.log(reply);
		}
	//close redis connection
		//client.quit();
	});
}

//call the function
createAndDisplayHash();
