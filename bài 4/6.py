int pos =0;
for(int i=s.length();i>=0;i--)
  if(s[i]==' '){
      pos=i;
      break;
    }
string ho=s.substr(0,pos);
string ten=s.substr(pos+1);
