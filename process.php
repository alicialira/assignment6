<?php
if (isset($_GET['integers']) && isset($_GET['threshold'])) {
    $integers = $_GET['integers'];
    $threshold = $_GET['threshold'];

    // Prepare data for Python script
    $input_data = json_encode(["integers" => $integers, "threshold" => $threshold]);

    // Call the Python script
    $command = escapeshellcmd("python3 bitwise_operations.py " . escapeshellarg($input_data));
    $output = shell_exec($command);

    // Display the output
    echo "<pre>$output</pre>";
} else {
    echo "Error: Missing input data.";
}
?>
