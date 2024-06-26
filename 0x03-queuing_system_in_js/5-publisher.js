import redis from 'redis';

const client = redis.createClient();

// Handles connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

function publishMessage(message, time) {
	//Indicates intent to publish after delay
	setTimeout(() => {
		console.log(`About to send ${message}`);

		//Publish message to channel
		client.publish('holberton school channel', message);
	}, time);
}

//Function calls
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
