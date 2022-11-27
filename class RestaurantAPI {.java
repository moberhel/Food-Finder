import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpClient;

class RestaurantAPI {

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://nutritionix-api.p.rapidapi.com/v1_1/search/xd?fields=item_name%2Citem_id%2Cbrand_name%2Cnf_calories%2Cnf_total_fat"))
		.header("X-RapidAPI-Key", "8249f77f64msh0340c24930fb03ap11c7dbjsnb0e487646a16")
		.header("X-RapidAPI-Host", "nutritionix-api.p.rapidapi.com")
		.method("GET", HttpRequest.BodyPublishers.noBody())
		.build();
        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());

    public static void main(String[] args) {
        System.out.println("hello world");

        

        
		
    }
}