
dependencias=(metasploit-framework gnome-terminal)

for programa in "${dependencias[@]}"; do
        if [ "$(command -v $programa)" ]; then
                echo "La herramienta $programa se encuentra instalada..."
                python3 msf-shell.py
                let counter+=1
                sudo su && bash add.sh
                echo "TOOL ADDED TO TERM"
                sleep 2
                
        else 
                echo "La herramienta $programa no se encuentra instalada..."
                echo "Instalando ahora..."
                sudo apt install gnome-terminal
                curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
                chmod 755 msfinstall && \
                ./msfinstall
                echo "Instaladas correctamente!"
                python3 msf-shell.py
                sudo su && bash add.sh
                echo "TOOL ADDED TO TERM"
                sleep 2
                
                
        fi; sleep 0.4
        
    done
        
        