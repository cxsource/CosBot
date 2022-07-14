using System.Collections.Specialized;

namespace HelheimExample
{
    public class TestClass
    {
        private static async Task<int> Main(string[] args)
        {
            await Helheim.Auth("xxxxxxxx", false);

            using var session = new Helheim.Session(new
            {
                browser = new
                {
                    browser = "chrome",
                    mobile = true,
                    platform = "windows"
                },
                debug = true
            });

            session.Wokou();

            session.SetHeaders(new OrderedDictionary
            {
                {
                    "User-Agent",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
                },
                { "x-kpsdk-v", "i-1.4.0" },
                { "client-brand", "apple" },
                { "accept", "*/*" },
                { "client-id", "00113916-3423-4120-b43a-b41ab413" },
                { "client-name", "veve-app-ios" },
                { "client-manufacturer", "apple" },
                { "client-model", "iphone 7 plus" },
                { "client-version", "1.0.539" }
            });

            dynamic kasadaHooks = new Dictionary<string, object>();
            kasadaHooks["mobile.api.prod.veve.me"] = new
            {
                POST = new[]
                {
                    "/graphql",
                    "/api/auth/*"
                }
            };

            session.SetKasadaHooks(kasadaHooks);

            await session.Request(new
            {
                method = "GET",
                url =
                    "https://mobile.api.prod.veve.me/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp",
                options = new { }
            });

            var response = await session.Request(new
            {
                method = "POST",
                url =
                    "https://mobile.api.prod.veve.me/graphql",
                options = new
                {
                    json = new
                    {
                        operationName = "AppMetaInfo",
                        variables = new { },
                        query =
                            "query AppMetaInfo { minimumMobileAppVersion featureFlagList { name enabled __typename} }"
                    }
                }
            });

            Console.WriteLine(response);

            return 0;
        }
    }
}