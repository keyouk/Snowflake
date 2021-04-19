import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Properties;
import java.util.TimeZone;


public class SnowflakeJDBCExample {
   public static void main(String[] args) throws Exception {
       // get connection
       System.out.println("Create JDBC connection");
       Connection connection = getConnection();
       System.out.println("Done creating JDBC connection\n");
       try {
           try {
                       Statement stmt = connection.createStatement();

                        //Table DDL: create table src_ts(col1 TIMESTAMP_NTZ);
                         ResultSet rs = stmt.executeQuery("INSERT QUERY HERE");

                        Object data = null;
                       int i = 1;
                        while(rs.next()) {
                                data = rs.getObject(i);
                               System.out.println(data);
                        }
                        //System.out.println(data);
                        rs.close();
                        stmt.close();
                }catch(SQLException e) {
                        e.printStackTrace();
                }
       } catch (Exception e) {
           e.printStackTrace();
       }
       connection.close();
       }
  private static Connection getConnection()
     throws SQLException {

   // build connection properties
   Properties properties = new Properties();
    
   String connectStr = " "; // "jdbc:snowflake://xy12345.snowflakecomputing.com";
   properties.put("user", "");         // replace "" with your user name
   properties.put("password", "");     // replace "" with your password
   properties.put("warehouse", "");    // replace "" with target warehouse name
   properties.put("db", "");           // replace "" with target database name
   properties.put("schema", "");       // replace "" with target schema name
   properties.put("TRACING", "ALL");   // if we need to enable logging, Comment this out if we don't need logs.


   return DriverManager.getConnection(connectStr, properties);
 }
}