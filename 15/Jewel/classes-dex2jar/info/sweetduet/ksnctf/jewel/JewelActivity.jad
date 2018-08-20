// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) 

package info.sweetduet.ksnctf.jewel;

import android.app.Activity;
import android.content.res.Resources;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.telephony.TelephonyManager;
import android.widget.ImageView;
import android.widget.Toast;
import java.io.InputStream;
import java.math.BigInteger;
import java.security.MessageDigest;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

// Referenced classes of package info.sweetduet.ksnctf.jewel:
//            b, a

public class JewelActivity extends Activity
{

    public JewelActivity()
    {
    }

    public void onCreate(Bundle bundle)
    {
        Object obj;
        super.onCreate(bundle);
        setContentView(0x7f030000);
        obj = ((TelephonyManager)getSystemService("phone")).getDeviceId();
        try
        {
            bundle = MessageDigest.getInstance("SHA-256");
            bundle.update(((String) (obj)).getBytes("ASCII"));
            bundle = (new BigInteger(bundle.digest())).toString(16);
            if(!((String) (obj)).substring(0, 8).equals("99999991"))
            {
                (new android.app.AlertDialog.Builder(this)).setMessage("Your device is not supported").setCancelable(false).setPositiveButton("OK", new b(this)).show();
                return;
            }
        }
        // Misplaced declaration of an exception variable
        catch(Bundle bundle)
        {
            Toast.makeText(this, bundle.toString(), 1).show();
            return;
        }
        if(!bundle.equals("356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5"))
        {
            (new android.app.AlertDialog.Builder(this)).setMessage("You are not a valid user").setCancelable(false).setPositiveButton("OK", new a(this)).show();
            return;
        }
        Object obj1 = getResources().openRawResource(0x7f040000);
        bundle = new byte[((InputStream) (obj1)).available()];
        ((InputStream) (obj1)).read(bundle);
        obj = new SecretKeySpec((new StringBuilder("!")).append(((String) (obj))).toString().getBytes("ASCII"), "AES");
        obj1 = new IvParameterSpec("kLwC29iMc4nRMuE5".getBytes());
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(2, ((java.security.Key) (obj)), ((java.security.spec.AlgorithmParameterSpec) (obj1)));
        bundle = cipher.doFinal(bundle);
        obj = new ImageView(this);
        ((ImageView) (obj)).setImageBitmap(BitmapFactory.decodeByteArray(bundle, 0, bundle.length));
        setContentView(((android.view.View) (obj)));
        return;
    }
}
