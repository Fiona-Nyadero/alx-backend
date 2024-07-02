import redis from 'redis';
import kue from 'kue';

const client = redis.createClient();

// Handles connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Create a Kue Queue
const queue = kue.createQueue();

queue.on('error', (err) => {
	console.error('Queue creation error:', err);
});

console.log('Queue created successfully');

// Define object
const jobData = {
	phoneNumber: '0745124162',
	message: 'Hello, I am Fiona! Nice to meet you!'
};

// Create a Job in the Queue
const neu_job = queue.create('push_notification_code', jobData)
	.save((err) => {
		if (err) {
			console.error('Error creating job:', err);
		} else {
			console.log('Notification job created:', neu_job.id);
		}
	});

// Job events
neu_job.on('complete', () => {
	console.log('Notification job completed');
});

neu_job.on('failed', (err) => {
	console.error('Notification job failed:', err);
});
