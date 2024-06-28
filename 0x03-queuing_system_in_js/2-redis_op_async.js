const { promisify } = require('util');
const redis = require('redis');
const client = redis.createClient();

// Handles connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

//Promisify get method
const getAsync = promisify(client.get).bind(client);

//Adds new Key-Value pair
function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

//Displays the Key-Value pairs
async function displaySchoolValue(schoolName) {
	try {
		const value = await getAsync(schoolName);
		console.log(value);
	} catch (error) {
		console.error(`Error retrieving value for ${schoolName}:`, error);
	}
}

//Call the Function
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
