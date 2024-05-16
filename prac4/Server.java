import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) {
        int portNumber = 8080;
        
        try (ServerSocket serverSocket = new ServerSocket(portNumber)) {
            System.out.println("Server is listening on port " + portNumber + "...");
            
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Connection established with " + clientSocket.getInetAddress().getHostAddress());
                
                new ClientHandler(clientSocket).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    private static class ClientHandler extends Thread {
        private Socket clientSocket;
        
        public ClientHandler(Socket socket) {
            this.clientSocket = socket;
        }
        
        @Override
        public void run() {
            try (
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()))
            ) {
                String inputLine;
                while ((inputLine = in.readLine()) != null) {
                    String reversedString = new StringBuilder(inputLine).reverse().toString();
                    out.println(reversedString);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
