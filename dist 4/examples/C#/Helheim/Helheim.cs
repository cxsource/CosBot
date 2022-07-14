using System.Collections.Specialized;
using System.Runtime.InteropServices;
using Newtonsoft.Json;

namespace HelheimExample
{
    public static class Helheim
    {
        [DllImport("helheim_cffi.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern IntPtr auth(string apiKey, bool discover);

        [DllImport("helheim_cffi.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern IntPtr getBalance();

        [DllImport("helheim_cffi.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern IntPtr createSession(string options);

        [DllImport("helheim_cffi.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern IntPtr deleteSession(int sessionId);

        [DllImport("helheim_cffi.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern IntPtr wokou(int sessionId, string browser);

        [DllImport("helheim_cffi.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern IntPtr bifrost(int sessionId, string libraryPath);

        [DllImport("helheim_cffi.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern IntPtr setHeaders(int sessionId, string headers);

        [DllImport("helheim_cffi.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern IntPtr setKasadaHooks(int sessionId, string kasadaHooks);

        [DllImport("helheim_cffi.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern IntPtr request(int sessionId, string options);

        [DllImport("helheim_cffi.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern IntPtr setProxy(int sessionId, string options);

        public class Session : IDisposable
        {
            private readonly int _sessionId;

            public Session(object options)
            {
                var response = createSession(JsonConvert.SerializeObject(options));
                if (response == IntPtr.Zero)
                    throw new NullReferenceException("Error -> createSession() -> NULL response detected");

                string responseString = Marshal.PtrToStringAnsi(response);
                dynamic result = JsonConvert.DeserializeObject(responseString);

                _sessionId = result.sessionID;
            }

            public dynamic Wokou(string browser = "chrome")
            {
                var response = wokou(_sessionId, browser);
                if (response == IntPtr.Zero)
                    throw new NullReferenceException("Error -> wokou() -> NULL response detected");

                string responseString = Marshal.PtrToStringAnsi(response);
                return JsonConvert.DeserializeObject(responseString);
            }

            public dynamic Bifrost(string libraryPath)
            {
                var response = bifrost(_sessionId, libraryPath);
                if (response == IntPtr.Zero)
                    throw new NullReferenceException("Error -> bifrost() -> NULL response detected");

                string responseString = Marshal.PtrToStringAnsi(response);
                return JsonConvert.DeserializeObject(responseString);
            }

            public dynamic SetHeaders(OrderedDictionary headers)
            {
                var response = setHeaders(_sessionId, JsonConvert.SerializeObject(headers));
                if (response == IntPtr.Zero)
                    throw new NullReferenceException("Error -> setHeaders() -> NULL response detected");

                string responseString = Marshal.PtrToStringAnsi(response);
                return JsonConvert.DeserializeObject(responseString);
            }

            public dynamic SetKasadaHooks(object kasadaHooks)
            {
                var response = setKasadaHooks(_sessionId, JsonConvert.SerializeObject(kasadaHooks));
                if (response == IntPtr.Zero)
                    throw new NullReferenceException("Error -> setKasadaHooks() -> NULL response detected");

                string responseString = Marshal.PtrToStringAnsi(response);
                return JsonConvert.DeserializeObject(responseString);
            }

            public async Task<dynamic> Request(object options)
            {
                var response = await Task.Run(() => request(_sessionId, JsonConvert.SerializeObject(options)));
                if (response == IntPtr.Zero)
                    throw new NullReferenceException("Error -> request() -> NULL response detected");

                string responseString = Marshal.PtrToStringAnsi(response);
                return JsonConvert.DeserializeObject(responseString);
            }

            public dynamic SetProxy(string proxy)
            {
                var response = setProxy(_sessionId, proxy);
                if (response == IntPtr.Zero)
                    throw new NullReferenceException("Error -> setProxy() -> NULL response detected");

                string responseString = Marshal.PtrToStringAnsi(response);
                return JsonConvert.DeserializeObject(responseString);
            }

            private void ReleaseUnmanagedResources()
            {
                deleteSession(_sessionId);
            }

            public void Dispose()
            {
                ReleaseUnmanagedResources();
                GC.SuppressFinalize(this);
            }

            ~Session()
            {
                ReleaseUnmanagedResources();
            }
        }

        public static async Task<dynamic> Auth(string apiKey, bool discover)
        {
            var response = await Task.Run(() => auth(apiKey, discover));
            if (response == IntPtr.Zero)
                throw new NullReferenceException("Error -> auth() -> NULL response detected");

            string responseString = Marshal.PtrToStringAnsi(response);
            return JsonConvert.DeserializeObject(responseString);
        }

        public static dynamic GetBalance()
        {
            var response = getBalance();
            if (response == IntPtr.Zero)
                throw new NullReferenceException("Error -> getBalance() -> NULL response detected");

            string responseString = Marshal.PtrToStringAnsi(response);
            return JsonConvert.DeserializeObject(responseString);
        }
    }
}
