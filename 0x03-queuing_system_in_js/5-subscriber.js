import redis from 'redis';

const client = redis.createClient();

// Handles connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

//Subscribe to channel
client.subscribe('holberton school channel')

//Handle unsubscription requests
client.on('message', (channel, message) => {
	console.log(`Recieved message from channel '${channel}': ${message}`);

	if (message === 'KILL_SERVER') {
		client.unsubscribe();
	}
});
