using System.IO.Ports;
using UnityEngine;

public class Serialcom : MonoBehaviour
{
    SerialPort serialPort = null;
    public string portName = "COM4";
    public int baudRate = 115200;
    int readTimeout = 50;

    public int data1;
    public int data2;

    void Start()
    {
        OpenConnection();
    }

    void OpenConnection()
    {
        if (serialPort != null)
        {
            if (serialPort.IsOpen)
            {
                Debug.Log("Serial port already open");
                return;
            }
            else
            {
                serialPort.Close();
                serialPort = null;
            }
        }

        try
        {
            serialPort = new SerialPort(portName, baudRate);
            serialPort.ReadTimeout = readTimeout;
            serialPort.Open();
        }
        catch (System.Exception e)
        {
            Debug.LogError("Error opening serial port: " + e.Message);
        }
    }
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            SendData(data1, data2);
        }
    }
    public void SendData(int data1, int data2)
    {
        if (serialPort != null && serialPort.IsOpen)
        {
            try
            {
                string message = $"{data1},{data2}";
                serialPort.WriteLine(message);
            }
            catch (System.Exception e)
            {
                Debug.LogError("Error sending data: " + e.Message);
            }
        }
        else
        {
            Debug.LogError("Serial port not open");
        }
    }
  

    void OnDisable()
    {
        if (serialPort != null && serialPort.IsOpen)
        {
            serialPort.Close();
        }
    }
}
