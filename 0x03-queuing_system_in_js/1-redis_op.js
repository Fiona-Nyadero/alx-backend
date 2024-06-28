import redis from 'redis';

const client = redis.createClient();

// Handles connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

//Adds new Key-Value pair
function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

//Displays the Key-Value pairs
function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, reply) => {
		if (err) {
			console.log(err);
		} else {
			console.log(reply);
		}
	});
}

//Call the Function
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
