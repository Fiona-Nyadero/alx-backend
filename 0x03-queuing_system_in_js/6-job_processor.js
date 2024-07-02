import kue from 'kue';

// Create a Kue Queue and handle creation errors
const queue = kue.createQueue();

queue.on('error', (err) => {
	console.error('Queue creation error:', err);
});

console.log('Queue created successfully');


// sendNotification function implementation
function sendNotification(phoneNumber, message) {
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process job Queue & handle errors
queue.process('push_notification_code', (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message);
	done();
});
