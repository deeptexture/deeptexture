using System.Collections;
using System.Collections.Generic;
using System.Drawing.Text;
using UnityEngine;
using System.IO.Ports;  



public class deeptextureserial : MonoBehaviour
{
    private static SerialPort sp;
    private static string incomingMsg = "";
    string[] split_data;

    // Start is called before the first frame update
    void Start()
    {
        sp = new SerialPort("COM5", 115200);
        sp.Open();
    }

    // Update is called once per frame
    void Update()
    {
        incomingMsg = sp.ReadTo("\n");
        
        //arduino should send data format like "20, 109\n"!
        //each data is saved in split_data
        split_data = incomingMsg.Split(',');
        incomingMsg = "";
    }

    private void OnApplicationQuit()
    {
        if(sp != null)
        {
            if (sp.IsOpen)
            {
                sp.Dispose();
                sp.Close();
            }
        }
        sp = null;
    }
}
