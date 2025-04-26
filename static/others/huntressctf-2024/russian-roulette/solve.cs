using System;
using System.Text;
using System.Security.Cryptography;
using System.Runtime.InteropServices;
using System.IO;
public class X
{
    public static unsafe string Shot()
    {
        bool o;
        uint r;
        byte[] c = Convert.FromBase64String("RNo8TZ56Rv+EyZW73NocFOIiNFfL45tXw24UogGdHkswea/WhnNhCNwjQn1aWjfw");
        byte[] k = Convert.FromBase64String("/a1Y+fspq/NwlcPwpaT3irY2hcEytktuH7LsY+NlLew=");
        byte[] i = Convert.FromBase64String("9sXGmK4q9LdYFdOp4TSsQw==");
        using (Aes a = Aes.Create())
        {
            a.Key = k;
            a.IV = i;
            ICryptoTransform d = a.CreateDecryptor(a.Key, a.IV);
            using (var m = new MemoryStream(c))
            using (var y = new CryptoStream(m, d, CryptoStreamMode.Read))
            using (var s = new StreamReader(y))
            {
                return s.ReadToEnd();
            }
        }
    }

    public static void Main()
    {
        string decryptedText = Shot();
        Console.WriteLine("Decrypted Text: " + decryptedText);
    }
}
