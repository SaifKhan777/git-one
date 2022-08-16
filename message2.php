
 <?php
 if(isset($_POST['abc'])){
     
    $mobile=$_POST['mobile'];
    $message=$_POST['message'];

    $fields = array(
        "message" => "due to traffic violation ,you have a fine of rs $message ,please pay at your nearest police station",
        "language" => "english",
        "route" => "q",
        "numbers" => "$mobile",
    );
    
    $curl = curl_init();
    
    curl_setopt_array($curl, array(
      CURLOPT_URL => "https://www.fast2sms.com/dev/bulkV2",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_SSL_VERIFYHOST => 0,
      CURLOPT_SSL_VERIFYPEER => 0,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode($fields),
      CURLOPT_HTTPHEADER => array(
        "authorization: OEp2maQrtATDUvKdwyCk7ZqWgLX4Iijb5sul09e16S8fNnYFohTtIdEr0hlaOMeL9Y2jRfFAKnNBwg5J",
        "accept: */*",
        "cache-control: no-cache",
        "content-type: application/json"
      ),
    ));
    
    $response = curl_exec($curl);
    $err = curl_error($curl);
    
    curl_close($curl);
    
    if ($err) {
      echo "cURL Error #:" . $err;
    } else {
      echo $response;
    }
 }
?>

