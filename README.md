<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Intercom System Documentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            text-align: center;
            background: linear-gradient(to bottom, purple, #2196F3);
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            height: 100vh;
            margin: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        h1 {
            color: #333333;
            padding-top: 40px;
            font-size: 50px;
        }

        .documentation {
            background-color: white;
            width: 80%;
            max-width: 800px;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
        }

        h2 {
            font-size: 24px;
            margin-top: 20px;
        }

        p {
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>Intercom System Documentation</h1>

    <div class="documentation">
        <h2>Introduction</h2>
        <p>
            This documentation provides information about the Intercom System, which includes a web interface for
            controlling the door's state, viewing live camera feed, and receiving email notifications when an unknown
            person attempts to enter. The system is designed to be user-friendly and efficient.
        </p>

        <h2>Features</h2>
        <ul>
            <li>Web Interface for Door Control</li>
            <li>Live Camera Feed</li>
            <li>Email Notifications for Unknown Visitors</li>
        </ul>

        <h2>Installation</h2>
        <p>
            To install and use the Intercom System, follow these steps:
        </p>
        <ol>
            <li>Clone the repository to your local machine.</li>
            <li>Install the required dependencies.</li>
            <li>Set up Firebase Admin credentials for database access.</li>
            <li>Add recognized faces to the "recognized" directory and encode them using the Face Recognition Library.</li>
            <li>Configure email settings for sending notifications.</li>
        </ol>

        <h2>Usage</h2>
        <p>
            To use the Intercom System:
        </p>
        <ol>
            <li>Run the Intercom System with the provided command.</li>
            <li>Access the web interface through your browser.</li>
            <li>Use the web interface to control the door state and view the live camera feed.</li>
            <li>When an unknown person is detected, the system will send an email notification to the owner.</li>
        </ol>

        <h2>Contributing</h2>
        <p>
            Contributions to this project are welcome. Follow these guidelines:
        </p>
        <ol>
            <li>Fork the repository on GitHub.</li>
            <li>Create a new branch from the master branch with a descriptive name.</li>
            <li>Make your changes and commit them.</li>
            <li>Push your changes to your forked repository.</li>
            <li>Create a pull request to merge your changes into the original repository.</li>
        </ol>

        <h2>License</h2>
        <p>
            This project is licensed under the XYZ License. See the LICENSE file for details.
        </p>

        <h2>Contact</h2>
        <p>
            For inquiries, contact [Your Name] at <a href="mailto:your.email@example.com">your.email@example.com</a>.
        </p>
    </div>
</body>
</html>

